Farmer Thomas is an edgy teenager who likes to ruin other people's dream of becoming a software engineer. Motivated by this, he attacked the Codewars servers with a strawberry baguette at 8:00 UTC on June 21 2022, and took down the Codewars website for an hour.

However, there was barely anyone online at that time, so Farmer Thomas' attack was very ineffective, as it affected very few people. Now, he wants your help in planning the next attack!

In the next `n` hours, the array `user_count` of length `n` stores the amount of people online at that hour. Farmer Thomas has enough money to attack the Codewars server for `k` hours (not necessarily in one consecutive attack though). He wants to plan the attack to affect as many people as possible.

However, the Codewars website has a backup battery that can keep the site running for two additional hours once an attack starts. This means that each period of attack must be more than 2 hours to have an actual effect. After the attack stops, Codewars will go back online and its backup battery will recharge instantly, ready for the next attack.

Take the following plan as example (✅ means Thomas is attacking at that hour, and ❌ means not attacking):
```
k = 7
user_count:        [ 30     10     0     100     200     300    20     10     30     1000 ]
should_attack:       ❌    ❌    ✅     ✅      ✅     ✅    ❌     ✅    ✅      ✅

affected_user_count: 200 + 300 + 1000 = 1500
```

In the above example, the sum of the duration of all the attacks is at most `k=7`, which can be arranged to be carried out anytime during the 10-hour time frame (as per the length of `user_count`). However, the first 2 hours in each consecutive period of attack do not affect the website (due to the backup battery) and thus do not add to the `total_affected_user`.

Given `user_count` and `k`, return the maximum amount of users that can be affected with the most optimal attacking plan. Good luck!

## Constraints
- `n < 500`
- `k < 250`
- 50 large tests
