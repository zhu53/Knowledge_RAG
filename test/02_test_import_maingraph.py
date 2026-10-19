import json
from asyncio import log

from tornado.process import task_id

from app.import_process.agent.main_graph import kb_import_app
from app.import_process.agent.state import create_default_state
import sys
from app.core.logger import logger

#1. 创建state
state = create_default_state(task_id="003", local_file_path="xxx.pdf")
#2. 执行编译后的图对象
result = kb_import_app.invoke(state)
logger.info(f"执行结果为{json.dumps(result, indent=4, ensure_ascii=False)}")
#3. 查看编译的图对象
logger.info(f"图编译结构: {kb_import_app.get_graph().print_ascii()}")