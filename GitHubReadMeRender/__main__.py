import argparse

from miniGHAPI.GitHubAPI import GHAPI

from . import getAndRenderReadMe

p = argparse.ArgumentParser(description="Renders readme of a GitHub repo in console")
p.add_argument("--format")
p.add_argument("repo")


def main():
	args = p.parse_args()
	owner, repo = args.repo.strip().split("/")

	gha = GHAPI("")
	r = gha.repo(owner, repo)

	rendered = getAndRenderReadMe(r)
	print(rendered)


if __name__ == "__main__":
	main()
