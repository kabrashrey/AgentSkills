---
name: check-weather
description: Get current weather, a 1-7 day forecast and short planning tips (umbrella, heat, cold, wind) for any city or lat/lon from the free Open-Meteo API, with no account or API key. Use when the user asks about the weather, rain, temperature or whether to plan around it, or when a briefing or trip plan needs a weather line.
metadata:
  version: "1.0"
---

# Check the weather

You are a weather helper: answer weather questions briefly and accurately from real forecast data, never from
memory or guesses.

## Inputs

- A place (city name, or latitude and longitude) and the day(s) asked about. If the place is missing, use the
  user's home city from their profile or memory; if that is unknown too, ask.
- Units: the user's preference from their profile or memory, else °F.

If you cannot run commands in this environment and no weather tool is available, say so at the start and ask the
user to check a forecast site.

## Ground rules

1. KEEP IT SIMPLE - NO OVER-ENGINEERING. This rule wins over all others.
2. WHEN IN DOUBT, ASK. Never guess; never present an assumption as a fact.
3. Use real data only. If the forecast call fails, say so plainly; never invent numbers.
4. Answer the question asked (e.g. "do I need an umbrella?" gets a yes/no first), then the supporting line.

## Steps

1. If your agent has a `weather_forecast` tool for the user's home city (some assistants do), call it for that
   city and go to step 3.
2. Otherwise run the bundled script, [scripts/forecast.py](scripts/forecast.py), with your terminal tool.
   `SKILL_DIR` is the folder containing this file. Python 3 standard library only:

   ```bash
   python3 SKILL_DIR/scripts/forecast.py --city "Los Angeles" --days 3
   python3 SKILL_DIR/scripts/forecast.py --lat 34.05 --lon -118.24 --days 1 --units c
   python3 SKILL_DIR/scripts/forecast.py --city "Paris" --days 2 --json
   ```

   Options: `--city`, or `--lat` with `--lon`; `--days 1-7` (default 1); `--units f|c` (default f); `--json` for
   machine-readable output. The first line names the place it matched: if that is the wrong place, ask the user
   for the state or country, or use `--lat/--lon`. Exit code 1 with `weather error: ...` means the lookup or the
   network failed.
3. Pick the day(s) the user asked about and answer.

## Output format

One short answer line first, then one line per day: `date: summary, high/low, rain %`, plus the tips the script
printed (umbrella at 40%+ rain, heat, cold morning, wind). Example:

```
No umbrella needed: Saturday looks dry.
2026-11-07: clear, high 83°F / low 69°F, rain 0% | hot: plan outdoor time early
```
