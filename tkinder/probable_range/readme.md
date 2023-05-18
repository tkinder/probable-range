# Project Name

The project fetches DJIA price data, sorts it, performs calculations, and outputs the results. It also creates a template and connects to the Blogger platform to create a blog post.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:

```sh
pip install -r requirements.txt
```

## Usage

To use the project, follow these steps:

1. Open the terminal and navigate to the project directory.
2. Run the following command:

```sh
python main.py
```

The program fetches DJIA data and outputs the following for last trading day:

- Open price
- High price
- Low price
- Closing deviation

Then calculates the following for the next trading day:

- Probable high price
- Probable low price

It also creates a blog post using a template and publishes it to the Blogger platform.

## Contributing

Contributions to the project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch and make your changes.
3. Push your changes to your forked repository.
4. Submit a pull request to the original repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
