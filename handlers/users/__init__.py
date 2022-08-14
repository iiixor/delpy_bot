from .help import dp
from .start import dp
from .info import dp
from .portfolio import dp
from .link import dp
from .switch_language import dp
from .echo import dp


# тут так скажем подключаем все хэндлеры, которые мы прописали в этой папке
# важно задать порядок выполнения, потому что хэндлеры всегда выполняются
# сверху-вниз
__all__ = ["dp"]
