#!/usr/bin/env python3
"""Weather forecast from Open-Meteo (free, no API key). Python standard library only.

    python3 forecast.py --city "Los Angeles" --days 3
    python3 forecast.py --lat 34.05 --lon -118.24 --units c --json

Prints current conditions, one line per day, and short planning tips (umbrella, heat, cold, wind).
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather interpretation codes (https://open-meteo.com/en/docs)
WMO = {0: "clear", 1: "mostly clear", 2: "partly cloudy", 3: "overcast", 45: "fog", 48: "freezing fog",
       51: "light drizzle", 53: "drizzle", 55: "heavy drizzle", 61: "light rain", 63: "rain", 65: "heavy rain",
       66: "freezing rain", 67: "heavy freezing rain", 71: "light snow", 73: "snow", 75: "heavy snow",
       77: "snow grains", 80: "light showers", 81: "showers", 82: "violent showers", 85: "snow showers",
       86: "heavy snow showers", 95: "thunderstorm", 96: "thunderstorm with hail", 99: "severe thunderstorm"}


def get_json(url: str, params: dict) -> dict:
    """GET url?params and parse the JSON reply."""
    req = urllib.request.Request(f"{url}?{urllib.parse.urlencode(params)}", headers={"User-Agent": "check-weather-skill"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def geocode(city: str) -> dict:
    """Best match for a place name: {name, lat, lon}."""
    hits = get_json(GEOCODE_URL, {"name": city, "count": 1, "format": "json"}).get("results") or []
    if not hits:
        raise ValueError(f"no place found for '{city}'")
    h = hits[0]
    label = ", ".join(x for x in (h.get("name"), h.get("admin1"), h.get("country_code")) if x)
    return {"name": label, "lat": h["latitude"], "lon": h["longitude"]}


def forecast(lat: float, lon: float, days: int, units: str) -> dict:
    """Current conditions plus daily rows from Open-Meteo, in the place's own timezone."""
    d = get_json(FORECAST_URL, {
        "latitude": lat, "longitude": lon, "timezone": "auto", "forecast_days": days,
        "temperature_unit": "fahrenheit" if units == "f" else "celsius",
        "wind_speed_unit": "mph" if units == "f" else "kmh",
        "current": "temperature_2m,weather_code",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max"})
    day = d["daily"]
    rows = [{"date": day["time"][i], "summary": WMO.get(day["weather_code"][i], f"code {day['weather_code'][i]}"),
             "high": day["temperature_2m_max"][i], "low": day["temperature_2m_min"][i],
             "rain_pct": day["precipitation_probability_max"][i], "wind_max": day["wind_speed_10m_max"][i]}
            for i in range(len(day["time"]))]
    cur = d.get("current", {})
    return {"timezone": d.get("timezone"), "now": {"temp": cur.get("temperature_2m"),
            "summary": WMO.get(cur.get("weather_code"), "unknown")}, "days": rows}


def tips(row: dict, units: str) -> list[str]:
    """Short planning hints for one day."""
    hot, cold, windy = (90, 45, 25) if units == "f" else (32, 7, 40)
    out = []
    if (row["rain_pct"] or 0) >= 40:
        out.append("take an umbrella")
    if row["high"] is not None and row["high"] >= hot:
        out.append("hot: plan outdoor time early")
    if row["low"] is not None and row["low"] <= cold:
        out.append("cold morning: bring a jacket")
    if (row["wind_max"] or 0) >= windy:
        out.append("windy")
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Open-Meteo forecast (no API key)")
    p.add_argument("--city", help="place name, e.g. 'Los Angeles'")
    p.add_argument("--lat", type=float)
    p.add_argument("--lon", type=float)
    p.add_argument("--days", type=int, default=1, help="1-7 (default 1)")
    p.add_argument("--units", choices=["f", "c"], default="f")
    p.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = p.parse_args()
    try:
        if a.lat is not None and a.lon is not None:
            place = {"name": f"{a.lat:.3f},{a.lon:.3f}", "lat": a.lat, "lon": a.lon}
        elif a.city:
            place = geocode(a.city)
        else:
            p.error("give --city or both --lat and --lon")
        fc = forecast(place["lat"], place["lon"], max(1, min(a.days, 7)), a.units)
    except Exception as e:  # network, bad place name, API change
        print(f"weather error: {e}", file=sys.stderr)
        return 1
    if a.json:
        print(json.dumps({"place": place["name"], **fc}, indent=1))
        return 0
    deg = "°F" if a.units == "f" else "°C"
    print(f"{place['name']} ({fc['timezone']}) now: {fc['now']['temp']}{deg}, {fc['now']['summary']}")
    for r in fc["days"]:
        extra = tips(r, a.units)
        print(f"{r['date']}: {r['summary']}, high {r['high']}{deg} / low {r['low']}{deg}, rain {r['rain_pct']}%"
              + (f" | {'; '.join(extra)}" if extra else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
