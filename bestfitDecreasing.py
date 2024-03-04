def best_fit_decreasing(items, bin_capacity):
  """
  Performs bin packing using the best-fit decreasing algorithm.

  Args:
      items: A list of item sizes.
      bin_capacity: The capacity of each bin.

  Returns:
      A list of lists,where each sublist represents the items in a bin.
  """
  # Sort items in decreasing order
  items.sort(reverse=True)

  # Initialize empty bins
  bins = []

  # Loop through each item
  for item in items:
    found_bin = False
    # Iterate through existing bins
    for bin in bins:
      # Check if item fits in the current bin
      if item <= bin_capacity - sum(bin):
        bin.append(item)
        found_bin = True
        break

    # If no existing bin fits the item, create a new bin
    if not found_bin:
      bins.append([item])

  return bins

# Example usage
items = [19, 15, 12, 9, 8, 7, 6, 4, 3, 2, 1]
bin_capacity = 20

bins = best_fit_decreasing(items, bin_capacity)

print("Items packed in bins:")
for i, bin in enumerate(bins):
  print(f"Bin {i+1}: {bin}")