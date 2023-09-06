import { writable } from 'svelte/store';

let stops = writable(
    [
        writable([0,0,0]),
        writable([0,0,0])
    ]
);


export default stops;

