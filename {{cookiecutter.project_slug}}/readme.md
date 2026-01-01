# {{ cookiecutter.project_name }}

A [pyview](https://pyview.rocks) project with [Web Awesome](https://webawesome.com/) components.

## Quick Start

```sh
just start
```

Then open http://localhost:{{ cookiecutter.port }} to see your app. A virtual environment will be created automatically.

## Commands

| Command | Description |
|---------|-------------|
| `just start` | Run dev server with hot reload |
| `just test` | Run tests |
| `just type-check` | Run type checking |
| `just add-view name` | Scaffold a new view |
| `just docker-build` | Build Docker image |
| `just docker-run` | Run Docker container |

## Docker

```sh
just docker-build
just docker-run
```

## Production

Set `PYVIEW_SECRET` for session security:

```sh
export PYVIEW_SECRET=$(openssl rand -base64 32)
```

## Learn More

- [pyview documentation](https://pyview.rocks)
- [Getting started guide](https://pyview.rocks/getting-started/)
- [Web Awesome components](https://webawesome.com/)
