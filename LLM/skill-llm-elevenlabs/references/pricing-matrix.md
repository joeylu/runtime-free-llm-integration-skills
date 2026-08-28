# ElevenLabs Pricing Matrix

Read `../../_shared/pricing-matrix-schema.md` first.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Billing Plan | Service Tier | List Unit Price | Effective Unit Price | Discount Kind | Valid From | Valid Until | Cache Class | Multiplier | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `speech` | `eleven_v3` | `global` | `USD` | `per-thousand-characters` | `output` | `TTS generated characters` | `all maintained HTTP TTS/dialogue routes` | `real-time` | `standard` | `0.10` | `0.10` | `none` | `unknown` | `open-ended` | `none` | `1` | `Multilingual v2/v3 API price; plan/tier included allowances vary by subscription.` | `2026-08-23` | `https://elevenlabs.io/pricing/api` |
| `speech` | `eleven_v3` | `global` | `USD` | `per-million-characters` | `output` | `Text-to-Dialogue WebSocket characters` | `dialogue-websocket only` | `real-time` | `beta` | `70` | `70` | `none` | `unknown` | `unknown` | `none` | `1` | `Beta Service guide states $70/1M chars starting on the next billing date unless otherwise agreed with account owner; product access is separately required.` | `2026-08-23` | `https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd` |
| `transcription` | `scribe_v2` | `global` | `USD` | `per-hour` | `audio` | `base transcription` | `all` | `batch` | `standard` | `0.22` | `0.22` | `none` | `unknown` | `open-ended` | `none` | `1` | `Multichannel bills each channel for full duration.` | `2026-08-23` | `https://elevenlabs.io/pricing/api` |
| `transcription` | `scribe_v2` | `global` | `USD` | `per-hour` | `audio` | `entity detection add-on` | `when entity detection is enabled` | `batch` | `standard` | `0.070` | `0.070` | `none` | `unknown` | `open-ended` | `none` | `1` | `Additional to base transcription. The endpoint reference separately describes a +30% surcharge; do not recompute from the base rate because that percentage does not exactly equal the pricing-page absolute figure.` | `2026-08-23` | `https://elevenlabs.io/pricing/api ; https://elevenlabs.io/docs/api-reference/speech-to-text/convert` |
| `transcription` | `scribe_v2` | `global` | `USD` | `per-hour` | `audio` | `keyterm prompting add-on` | `when keyterms are enabled` | `batch` | `standard` | `0.050` | `0.050` | `none` | `unknown` | `open-ended` | `none` | `1` | `Additional to base transcription; endpoint has separate minimum-billing behavior for >100 keyterms. The endpoint reference also describes a +20% surcharge; do not recompute from the base rate because that percentage does not exactly equal the pricing-page absolute figure.` | `2026-08-23` | `https://elevenlabs.io/pricing/api ; https://elevenlabs.io/docs/api-reference/speech-to-text/convert?explorer=true` |

## Rules

- Do not use Scribe v2 Realtime pricing for `scribe_v2`.
- Do not treat the Beta Text-to-Dialogue WebSocket price as the ordinary HTTP v3 TTS price.
- Subscription included quantities and plan-specific tier entitlements are not modeled as universal discounts here.
- Refresh this matrix before a cost-sensitive production change because provider prices can change independently of model IDs.
