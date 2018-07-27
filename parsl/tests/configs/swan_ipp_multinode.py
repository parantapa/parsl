"""
    Block
====================================
| ++++++++++++++ || ++++++++++++++ |
| |    Node    | || |    Node    | |
| |            | || |            | |
| | Task  Task | || | Task  Task | |
| |            | || |            | |
| ++++++++++++++ || ++++++++++++++ |
====================================
"""
from libsubmit.channels import SSHChannel
from libsubmit.launchers import AprunLauncher
from libsubmit.providers import TorqueProvider

from parsl.config import Config
from parsl.executors.ipp import IPyParallelExecutor
from parsl.executors.ipp_controller import Controller

from parsl.tests.utils import get_rundir

# CAUTION: Make sure to setup user_opts.py
from .user_opts import user_opts

config = Config(
    executors=[
        IPyParallelExecutor(
            label='swan_ipp',
            provider=TorqueProvider(
                channel=SSHChannel(
                    hostname='swan.cray.com',
                    username=user_opts['swan']['username'],
                    script_dir=user_opts['swan']['script_dir'],
                ),
                nodes_per_block=2,
                tasks_per_node=2,
                init_blocks=1,
                max_blocks=1,
                launcher=AprunLauncher(),
                overrides=user_opts['swan']['overrides']
            ),
            controller=Controller(public_ip=user_opts['public_ip']),
        )

    ],
    run_dir=get_rundir()
)
