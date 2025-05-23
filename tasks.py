from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage, optional=["mode"])
def coverage_report(ctx, mode="html"):
    ctx.run(f"coverage {mode}", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
