#!/usr/bin/env python3
import argparse
from animate import animate,ALGORITHMS
# animate("Shell Sort", n=500, sequence="ciura",speed=100)
animate("Heap Sort", n=500)

def args():
    """
    Parse command-line arguments and return the Namespace object.
    """
    parser = argparse.ArgumentParser(
        description="Visualize sorting algorithms with customizable parameters"
    )
    parser.add_argument(
        "algorithm",
        choices=list(ALGORITHMS.keys()),
        help="Sorting algorithm to visualize (e.g., 'Heap Sort', 'Shell Sort')"
    )
    parser.add_argument(
        "-n", "--n",
        type=int,
        default=50,
        help="Number of elements in the array (default: 50)"
    )
    parser.add_argument(
        "-s", "--speed",
        type=int,
        default=10,
        help="Animation speed from 1 (slow) to 100 (fast) (default: 10)"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=600,
        help="Width of the window in pixels (default: 600)"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=400,
        help="Height of the window in pixels (default: 400)"
    )
    parser.add_argument(
        "--sequence",
        type=str,
        help="Custom sequence for algorithms like Shell Sort (e.g., 'ciura')"
    )
    return parser.parse_args()

def main():
    # Parse arguments
    args_ns = args()

    # Prepare kwargs for algorithm-specific parameters
    kwargs = {}
    if args_ns.sequence:
        kwargs['sequence'] = args_ns.sequence

    # Launch the visualization
    animate(
        args_ns.algorithm,
        n=args_ns.n,
        speed=args_ns.speed,
        width=args_ns.width,
        height=args_ns.height,
        **kwargs
    )


if __name__ == "__main__":
    main()
