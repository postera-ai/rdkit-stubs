LINEEND: str

def cacheImageFile(filename) -> None: ...
def preProcessImages(spec) -> None: ...
def cachedImageExists(filename): ...
def _escape(s): ...
def _normalizeLineEnds(text, desired=...): ...
def _AsciiHexEncode(input): ...
def _AsciiHexDecode(input): ...
def _AsciiHexTest(text: str = ...) -> None: ...
def _AsciiBase85Encode(input): ...
def _AsciiBase85Decode(input): ...
def _wrap(input, columns: int = ...): ...
def _AsciiBase85Test(text: str = ...) -> None: ...
