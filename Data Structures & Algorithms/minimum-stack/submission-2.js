class MinStack {
    constructor() {
        this.stack = []
        this.min = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        if (this.min.length === 0 || val <= this.min.at(-1)) {
            this.min.push(val)
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const last = this.stack.pop()
        if (last === this.min.at(-1)) {
            this.min.pop()
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack.at(-1)
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min.at(-1)
    }
}
