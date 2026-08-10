import time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        start_time = time.time()
        results = self._expensive_computation(self.data)
        duration = time.time() - start_time
        print(f"Data processed in {duration:.4f} seconds.")
        return results

    def _expensive_computation(self, data):
        # Simulate an expensive operation
        processed = [d * 2 for d in data]
        time.sleep(1)  # Simulate delay
        return processed

    def batch_process(self, batch_size):
        results = []
        batches = [self.data[i:i + batch_size] for i in range(0, len(self.data), batch_size)]
        for batch in batches:
            results.extend(self.process_data(batch))
        return results

if __name__ == "__main__":
    processor = DataProcessor(range(100))
    final_results = processor.batch_process(10)
    print(final_results)