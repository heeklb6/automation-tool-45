from typing import Any, Dict, List

def calculate_average(prices: List[float]) -> float:
    """
    Calculate the average of a list of prices.

    Args:
        prices (List[float]): A list of price values.

    Returns:
        float: The average price.
    """
    if not prices:
        return 0.0
    return sum(prices) / len(prices)


def filter_prices(prices: List[float], threshold: float) -> List[float]:
    """
    Filter prices that are above a given threshold.

    Args:
        prices (List[float]): A list of price values.
        threshold (float): The threshold to filter prices.

    Returns:
        List[float]: A list of prices above the threshold.
    """
    return [price for price in prices if price > threshold]


def convert_to_dict(items: List[str], values: List[Any]) -> Dict[str, Any]:
    """
    Convert two lists into a dictionary.

    Args:
        items (List[str]): A list of keys.
        values (List[Any]): A list of values corresponding to the keys.

    Returns:
        Dict[str, Any]: A dictionary mapping keys to values.
    """
    return dict(zip(items, values))
