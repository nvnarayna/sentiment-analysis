<script lang='ts'>
import stops from "./store";
import sentiment from "./store2";
import fetch_sentiment from "./fetch";

let txt:string =""

let set_start= (idx,val) => {
    $stops[0][idx]=val
    $stops=$stops
}
let set_stops= (idx,val) => {
    $stops[1][idx]=val
    $stops=$stops
}
let set_data=(data)=>{
    set_start(0,0)
    set_stops(0,data.pos)
    set_start(1,data.pos)
    set_stops(1,data.pos+data.neg)
    set_start(2,data.pos+data.neg)
    set_stops(2,100)
    
}
let set_sentiment=(snmt)=>{
    $sentiment[0]=snmt
    if (snmt == "Positive"){
        $sentiment[1]="text-success-500"
    }else if (snmt=="Negative"){
        $sentiment[1]="text-success-500"
    }else{
        $sentiment[1]="text-warning-500"
    }
    $sentiment=$sentiment
}
let handle_click= async ()=>{
    if (txt !=""){
    let data=await fetch_sentiment(txt)
    set_data(data)
    set_sentiment(data.sentiment)
    txt=""
}
}
</script>



<input class="input w-11/12 m-3" type="text" bind:value={txt}  placeholder="Input" />
<button type="button" class="btn variant-filled " on:click={handle_click}>Button</button>
