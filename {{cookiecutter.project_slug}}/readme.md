# {{ cookiecutter.project_name }}

## Development

This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies and [just](https://github.com/casey/just) as a command runner.

### Running

```sh
just
```

This will run your pyview project using uvicorn with hot reloading on port {{ cookiecutter.port }}.

A virtual environment will automatically be created.

## Features

- **PyView**: Phoenix LiveView-inspired framework for Python
- **Web Awesome**: Modern web component library and design system
- **uv**: Fast Python package management
- **Just**: Simple command runner

## Available Commands

- `just` - Start development server with hot reload
- `just test` - Run tests with pytest
- `just type-check` - Run type checking with pyright
- `just add-view <name>` - Create a new view
- `just docker-build` - Build Docker image
- `just docker-run` - Run in Docker container
