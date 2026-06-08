# Fantasy Football 2026 — Draft Boards

Interactive draft prep + in-season surfaces for a 12-team ESPN PPR league.

**Live site:** enable GitHub Pages (Settings → Pages → Deploy from branch → `main` / root) and the boards are viewable at `https://<username>.github.io/<repo>/`.

| Surface | What it is |
|---|---|
| [Draft Board](Board/draft-board.html) | Big board — tiers, ADP, positional ranks, edge badges, draft mode |
| [Research Digest](Board/research-digest.html) | Player profiles + research notes |
| [In-Season Hub](Board/in-season-hub.html) | Weekly lineup + matchup view |

The HTML pages fetch `Data/players.csv` and the sidecar JSONs at load time, so they must be served over HTTP (GitHub Pages works; opening the files directly via `file://` won't load the data layer).

To update: replace the files in `Data/` (and the HTML if regenerated) and push.
