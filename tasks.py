from invoke import task

WATCH_COMMAND = "watchmedo shell-command --patterns '*.py' --drop --command='{}' src"


@task(optional=["watch"])
def start(ctx, watch=None):
    if not watch:
        return ctx.run("python3 src/main.py", pty=True)
    print(WATCH_COMMAND.format("invoke start"))
    ctx.run(WATCH_COMMAND.format("invoke start"), pty=True)


@task
def test(ctx):
    ctx.run("pytest", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage, optional=["watch", "mode"])
def coverage_report(ctx, watch=None, mode="html"):
    if not watch:
        return ctx.run(f"coverage {mode}", pty=True)
    ctx.run(WATCH_COMMAND.format("invoke coverage-report --mode report"), pty=True)
