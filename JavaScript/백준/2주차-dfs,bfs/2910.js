const hack = () => {
    let [[n, c], arr] = require("fs")
        .readFileSync("input.txt")
        .toString()
        .trim()
        .split("\n")
        .map((v) => v.split(" ").map(Number));
    let obj = {};
    for (let i = 0; i < n; i++) {
        if (!obj[arr[i]]) obj[arr[i]] = [i, 1];
        else obj[arr[i]][1]++;
    }

    console.log(
        Object.entries(obj)
            .sort((a, b) => {
                if (b[1][1] === a[1][1]) return a[1][0] - b[1][0];
                else return b[1][1] - a[1][1];
            })
            .map((v) => Array(v[1][1]).fill(v[0]).join(" "))
            .join(" ")
    );
};

hack();