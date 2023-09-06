import { writable } from "svelte/store"

let sentiment = writable(["",""]) //sentiment,color

export default sentiment;