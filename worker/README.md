# Developing algorithms

1. Create a module (e.g. fetch_polygon)
2. Run the module manually while developing, using `if __name__ == "__main__"`, command `python -m directory-name` (or use vs-code run menu).
3. Develop the algorithm to be executed by a single method (e.g. run_polygon) and use environment dependent settings as arguments
4. When the algorithm is working in manual mode, call it from `./algorithm-worker` in the `on_message` function. `job.Algorithm` need to be the same as in the algorithm config database.
