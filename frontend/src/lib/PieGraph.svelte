<script lang='ts'>
    import { ConicGradient } from '@skeletonlabs/skeleton';
    import type { ConicStop } from '@skeletonlabs/skeleton';
    import stops from './store';
    let conicStops: ConicStop[]
    $:conicStops = [
		{ label: 'positive', color: 'rgba(var(--color-success-500))', start:$stops[0][0] , end: $stops[1][0] },
		{ label: 'negative', color: 'rgba(var(--color-error-500))', start:$stops[0][1], end: $stops[1][1] },
		{ label: 'neutral', color: 'rgba(var(--color-warning-500))', start: $stops[0][2], end: $stops[1][2] }
];
    console.log(conicStops)
</script>




<ConicGradient stops={conicStops} legend>

</ConicGradient>