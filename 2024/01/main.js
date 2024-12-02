async function main() {
    const contents = await Bun.file("input.txt").text();
    const left = [];
    const right = [];
    for (const row of contents.split("\n")) {
        if (row === "") continue;
        const split = row.split(" ");
        left.push(Number(split[0]))
        right.push(Number(split[split.length - 1]))
    }
    left.sort();
    right.sort();

    let diff = 0;
    for (let i = 0; i < left.length; i++) {
        diff += Math.abs(left[i] - right[i])
    }
    console.log(diff);
}

async function second() {
    const contents = await Bun.file("input.txt").text();
    const left = [];
    const right = [];
    for (const row of contents.split("\n")) {
        if (row === "") continue;
        const split = row.split(" ");
        left.push(Number(split[0]))
        right.push(Number(split[split.length - 1]))
    }
    left.sort();
    right.sort();
    let counts = {};
    let count = 0;
    let previous = right[0];
    for (let i = 0; i < right.length; i++) {
        if (right[i] !== previous) {
            counts[previous] = count;
            count = 0;
        }

        count++;
        previous = right[i];
    }
    counts[previous] = count;

    let diff = 0;
    for (const l of left) {
        diff += (counts[l] ?? 0) * l
    }
    console.log(diff);
}

(async() => {
    await main();
    await second();
    process.exit(0);
})()
