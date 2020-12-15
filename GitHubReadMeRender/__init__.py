from pathlib import PurePath
from warnings import warn

from LMRender import SF, DEFAULT_RENDERER
from miniGHAPI.GitHubAPI import CT, Repo

__all__ = ("getAndRenderReadMe",)


def getAndRenderReadMe(repoObj: Repo, targetFormat: SF = SF.gfm_ansi):
	readMe = repoObj.getReadMe(accept=CT.json)

	rawSrc = readMe["$content"]
	fmt = SF.fromFileName(PurePath(readMe["name"]))
	unavail = DEFAULT_RENDERER.isSourceUnavailable(fmt)

	def fallback():
		nonlocal rawSrc, fmt
		rawSrc = repoObj.getReadMe(accept=CT.html)["$content"]
		fmt = SF.html

	if fmt is None:
		fallback()
	elif unavail:
		warn("Install " + " or ".join(unavail) + " to spare an API request. Requesting GitHub to render the ReadMe into HTML.")
		fallback()

	return DEFAULT_RENDERER.render(rawSrc, fmt, targetFormat)
