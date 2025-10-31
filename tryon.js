import { Client } from "@gradio/client";

async function runPrediction() {
    const client = await Client.connect("levihsu/OOTDiffusion");
    const result = await client.predict("/process_hd", {
        vton_img: modelImage,
        garm_img: garmentImage,
        n_samples: 1,
        n_steps: 20,
        image_scale: 1,
        seed: -1,
    });
    console.log(result);
}

runPrediction();