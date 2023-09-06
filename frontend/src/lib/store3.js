import { writable } from "svelte/store"

let prev_prompt= writable("") //sentiment,color

export default prev_prompt;