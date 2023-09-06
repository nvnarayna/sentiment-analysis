<script lang='ts'>
import PieGraph from "$lib/PieGraph.svelte";
import sentiment from "./store2";
import prev_prompt from "./store3";
let color_class
let color
let snmt
$:color_class='h4 text-center '+{color}
$:snmt=$sentiment[0]
$:color=$sentiment[1]
</script>

{#if $sentiment[0]!=""}
<div class='card m-2 p-4'>
    <h1 class="h5 text-center" >prompt:{$prev_prompt}</h1>
    <h1 class={color_class} >sentiment:{snmt}</h1>
    <PieGraph/>
</div>
{/if}

