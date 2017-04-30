from behave import given

import os
import shlex
import shutil
import subprocess as sp
import sure

@given(u'a fresh machine with mkdo installed')
def step_impl(context):
    docker_dir = 'docker'
    docker_name = 'mkdo/acceptance-test-run'
    shutil.rmtree(docker_dir, ignore_errors=True)
    os.mkdir(docker_dir)
    shutil.copy('../dist/mkdo-0.1.0-py2.py3-none-any.whl', os.path.join(docker_dir))
    with open(os.path.join(docker_dir, 'Dockerfile'), 'w') as f:
        f.write("""
FROM debian:8.5

#RUN apt-get update \
# && apt-get install -y --no-install-recommends \
#        ca-certificates \
#        curl \
# && rm -rf /var/lib/apt/lists/* \
# && apt-get clean

ADD mkdo-0.1.0-py2.py3-none-any.whl /tmp/foo
""")

    #assert 0 == sp.call(['docker', 'build', '-t', docker_name, docker_dir], stdout=sp.PIPE)
    return_code = sp.call(['docker', 'build', '-t', docker_name, docker_dir], stdout=sp.PIPE)
    return_code.should.be(0)
    context.docker_name = docker_name

@given(u'an empty source directory')
def step_impl(context):
    context.fake_srcdir = os.path.join(os.getcwd(), 'fake_srcdir')
    os.mkdir(context.fake_srcdir)

@when(u'the user runs "{}"')
def step_impl(context, command):
    args = shlex.split(command)
    p = sp.Popen(['docker', 'run', '--rm',
                  '--volume=%s:%s:rw' % (context.fake_srcdir, context.fake_srcdir),
                  '--workdir=%s' % (context.fake_srcdir,),
                  context.docker_name] + args,
                 stdout=sp.PIPE, stderr=sp.PIPE)
    context.stdout, context.stderr = p.communicate()
    context.returncode = p.returncode

@then(u'a "do/build" script is created')
def step_impl(context):
    os.path.exists(os.path.join(context.fake_srcdir, 'do')).should.be.true
