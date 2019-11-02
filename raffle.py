# Beyondcoin Raffle Script

import random
import time
import sys
from progress.bar import Bar

ADDRESSES = [
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'CoinInfo [B6DMvJDzMmPjwbdkQg5UsoiYCsbkQ9Xzfi]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'NeroZyF [B8YtTvwg4jYM8E9NTNjEmR4VjPzpUkEveS]',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Wheeler',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Jonn4y',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'Mc | So Kanon',
'GOOFUS',
'GOOFUS',
'GOOFUS',
'GOOFUS',
'GOOFUS',
'Octl',
'Octl',
'Octl',
'Octl',
'Octl'
]

beyondcoin_amount = '10000'
address_total = '7'
ticket_count = '320'
prize_count = '23'

print("Welcome to the...")

time.sleep(1)

print("""\n\
#####################################################################################################################
*  ____  ________     ______  _   _ _____   _____ ____ _____ _   _    _____            ______ ______ _      ______  *
* |  _ \|  ____\ \   / / __ \| \ | |  __ \ / ____/ __ \_   _| \ | |  |  __ \     /\   |  ____|  ____| |    |  ____| *
* | |_) | |__   \ \_/ / |  | |  \| | |  | | |   | |  | || | |  \| |  | |__) |   /  \  | |__  | |__  | |    | |__    *
* |  _ <|  __|   \   /| |  | | . ` | |  | | |   | |  | || | | . ` |  |  _  /   / /\ \ |  __| |  __| | |    |  __|   *
* | |_) | |____   | | | |__| | |\  | |__| | |___| |__| || |_| |\  |  | | \ \  / ____ \| |    | |    | |____| |____  *
* |____/|______|  |_|  \____/|_| \_|_____/ \_____\____/_____|_| \_|  |_|  \_\/_/    \_\_|    |_|    |______|______| *
*                                                                                                                   *
#####################################################################################################################
""")

time.sleep(1.75)

print("There are " + beyondcoin_amount  + " Beyondcoins in prizes to giveaway, " + address_total  + " participants, and " + ticket_count + " tickets in this raffle.")

time.sleep(2)

print("\nThe Beyondcoins will be distributed to " + prize_count  + " randomly selected people.")

time.sleep(1.25)

print("""\

        PRIZE TABLE
 _________________________
|                         |
|    Amount  || # Prizes  |
| ===========||========== |
|    2500    ||    3      |
|     250    ||    5      |
|     100    ||    10     |
|      50    ||    5      |
|_________________________|
""")

#print("\n")

time.sleep(1.5)

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("The drawing will start in {:2d} seconds!".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

print("\n\nThe 2,500 BYND drawing with a total of 3 prizes, has started...")

time.sleep(3)

print("\n")

bar = Bar('and the first 2,500 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the second drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the second 2,500 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the final drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the third and final Beyondcoin raffle winner is...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!\n\n".format(random.choice(ADDRESSES)))

print("*************************************************************************")

time.sleep(2)

print("\nNow drawing for 250 BYND with 5 prizes available...")
print("\n")

time.sleep(1.25)

bar = Bar('and the first 250 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the second 250 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the second 250 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the third 250 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the third 250 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fourth 250 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the fourth 250 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fianl 250 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the final 250 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!\n\n".format(random.choice(ADDRESSES)))

print("*************************************************************************")

print("\nNow drawing for 100 BYND with 10 prizes available...")
print("\n")

time.sleep(1.25)

bar = Bar('and the first 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the second 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the second 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the third 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the third 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fourth 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the fourth 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fifth 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the fifth 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the sixth 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the sixth 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the seventh 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the seventh 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the eighth 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the eighth 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the ninth 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the ninth 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fianl 100 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the final 100 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!\n\n".format(random.choice(ADDRESSES)))

print("*************************************************************************")

time.sleep(2)

print("\nNow drawing for 50 BYND with 5 prizes available...")
print("\n")

time.sleep(1.25)

bar = Bar('and the first 50 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the second 50 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the second 50 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the third 50 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the third 50 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fourth 50 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the fourth 50 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the fianl 50 BYND drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the final 50 BYND prize goes to...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!\n\n".format(random.choice(ADDRESSES)))

print("-" * 75 + "\n")

time.sleep(1)

print("Congratulations to everyone that won!")
print("\nThank you to eveyone that participated in the Beyondcoin raffle!")
print("\n")
