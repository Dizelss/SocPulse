from .celery_app import app
from .channel_info import get_channel_info, update_channel_info


@app.task(name="tg_names_to_analyze")
def tg_names_to_analyze(tg_name, start0, start1):
    result_info_channel = get_channel_info(start0, tg_name)
    update_channel_info(result_info_channel, start1)
    return f"задача выполнена, {result_info_channel}"
