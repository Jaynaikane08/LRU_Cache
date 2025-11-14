LRU Cache (Python Implementation)

This project explains the working of a simple Least Recently Used (LRU) Cache. An LRU cache automatically removes the least recently used item when it reaches its maximum capacity.

📌 Overview

An LRU Cache is a caching technique that keeps the most recently or frequently used items easily accessible. When the cache becomes full and a new item needs to be added, the item that has been used the least is removed.

🔧 How This Implementation Works

-The cache has a fixed capacity of 4 items.

-Each incoming request is processed as follows:

-If the cache has space → the item is added.

-If the item already exists → its usage count is increased.

-If the cache is full and the item does not exist → the system finds the item with the lowest usage count and removes it.

-Every item in the cache has:

-A key → representing the request

-A value → representing how many times that item has been used

📊 Behavior Summary

-The cache functions like a dictionary.

-Usage count helps decide which item is the least recently used.

-When the cache reaches full capacity:

-Items with higher usage stay longer

-The item with the smallest usage count gets removed first

-This simulates an LRU mechanism based on access frequency.

🚀 Key Features

-Simple explanation of LRU functionality

-Easy-to-understand logic suitable for beginners

-Demonstrates eviction based on least usage

-Helps in understanding caching strategies often used in system design and interviews

🌱 Future Improvements

-Convert logic into a class-based implementation

-Use OrderedDict for true LRU handling

-Add unit tests for reliability

-Make cache size configurable

-Track recent access order in addition to usage count

📘 Purpose

This project serves as an introductory example of how LRU caching works.
It is ideal for:

-Students

-Interview preparation

-Understanding basic caching techniques

-Beginners exploring Python logic and data structures
