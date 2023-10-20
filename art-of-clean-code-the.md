# Chapter 4

## Writing Clean Code: The Principles

1. **Think About the Big Picture**
2. **Stand on the Shoulders of Giants**
   - Use libraries.
3. **Code for People, Not Machines**
   - People, including your future self.
4. **Use the Right Names**
   - **4.1 Descriptive Names**
     - Clearer is better: `usd_to_eur(amount)` > `dollar_to_euro(amount)`
   - **4.2 Unambiguous Names**
   - **4.3 Pronounceable Names**
   - **4.4 Named Constants, Not Magic Numbers**
5. **Adhere to Standards**
6. **Use Comments**
   - But don't overdo it.
7. **Avoid Unnecessary Comments**
   - Don't comment what's self-explanatory; it may confuse and clutter, making code harder to read.
8. **The Principle of Least Surprise**
9. **Don't Repeat Yourself (DRY)**
   - "WET" - Waste Everyone's Time.
10. **Single Responsibility Principle**
11. **Test**
12. **Small is Beautiful**
   - Avoid "God Objects" / monolithic code blocks.
13. **The Law of Demeter**
   - An object should only communicate with its immediate neighbors.
14. **You Ain't Gonna Need It**
15. **Don't Use Too Many Levels of Indentation**
16. **Use Metrics**
   - To track complexity.
17. **Boy Scout Rule and Refactoring**
   - "Leave the campground cleaner than you found it."

# Chapter 7

## 15 Useful Unix Principles


1. **Make each function do one thing well**
2. **Simple is better than complex**
3. **Small is beautiful**
  - further reading: https://martinfowler.com/articles/microservices.html
4. **Build a prototype as soon as possible**
5. **Choose portability over efficiency**
6. **Store data in flat text files**
  - CSV
  - Database (optimization) for larger projects.
