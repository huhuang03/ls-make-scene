from pathlib import Path

from .config import META_CONTENT_KEY, MARK_SCENE_URL_PREFIX
from img_collector import Image


def get_img_db_path() -> Path:
    rst = Path(__file__).parent.parent.parent.parent / 'imgs/images.db'
    assert rst.exists()
    return rst.absolute()


def get_meta_content_key_from_task(task):
    if not task:
        return None
    return task.meta and task.meta[META_CONTENT_KEY]


def image_to_data(img: Image):
    return {'image': concat_url(MARK_SCENE_URL_PREFIX, img.dst_path)}


def fix_url(src: str) -> str:
    return src.replace("//", "/")


def concat_url(*parts: str) -> str:
    return fix_url('/'.join(parts))
