TEST_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} || true
	find . -name '*.pyo' -exec rm --force {} || true

setup:
	bash bin/setup-local.sh

tests: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

run: clean-pyc
	python main.py --image ./assets/crosses.jpg

docker-run:
	echo "Coming soon"