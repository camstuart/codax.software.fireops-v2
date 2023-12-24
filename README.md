# fireops

FastAPI, Piccolo ORM, SvelteKit UI


## Initial Setup (Python)

```bash
poetry init
poetry config --local virtualenvs.in-project true
poetry add "piccolo[postgres]"
poetry shell
piccolo app new database
piccolo show_all
piccolo migrations new --auto --app_name=database
piccolo migrations check
piccolo migrations forwards database
```

## Initial Setup (SvelteKit)

```bash
...
```

## TODO

- [ ] Add authentication with [this guide](https://mainmatter.com/blog/2023/11/23/setting-up-oauth-with-auth-js-and-sveltekit/)
- [ ] Create the "Incident" table (no postgis for now)
- [ ] Create a loader script for "Incident", and load some data
- [ ] Create the "Incident" API Endpoint
- [ ] Display incidents in the UI (authenticated users only)
- [ ] Build the audio player
- [ ] Setup supabase as the production database, and run migrations, seed data
- [ ] Create Dockerfile for api containerisation
- [ ] Setup a Github action to deploy the UI to Vercel, and backend somewhere? (railway)