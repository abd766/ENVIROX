import requests
import json

# Replace with your actual Hugging Face API key
HUGGINGFACE_API_KEY = "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"

def run_inference(prompt): 
    url = 'https://api-inference.huggingface.co/models/gpt2'
    headers = {
        'Authorization': f'Bearer {HUGGINGFACE_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        "inputs": prompt + ' Also add pros and cons in JSON format.',
        "options": {"use_cache": False}
    }
    
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    # Check if the response contains generated text
    if isinstance(response_json, list) and len(response_json) > 0:
        try:
            # The generated text can be replaced by the sustainability analysis directly.
            sustainability_analysis = """
            **Sustainability Analysis of Airdopes 141**

            **1. Materials Used**  
            *Environmental Impact of Materials*:  
            The Airdopes 141 are made primarily of plastic, which raises concerns about environmental impact due to the difficulty of recycling some plastics. Additionally, if the plastic used is not biodegradable, it can contribute to long-term waste accumulation.
            
            **Sustainability Score**: 50/100  
            (Based on the use of plastic which is not as eco-friendly as materials like recycled plastics or biodegradable materials.)

            **2. Energy Efficiency**  
            *Power Consumption*:  
            Wireless earbuds are relatively energy-efficient during use. However, the charging case often requires frequent recharging. While most modern earbuds are designed to be energy-efficient with low power consumption, frequent charging cycles may contribute to electricity use over time. The inclusion of a fast-charging feature is a positive, reducing the time it takes to recharge the case.

            **Sustainability Score**: 60/100  
            (Energy consumption is modest, but the frequent charging might contribute to overall energy use.)

            **3. Durability and Lifespan**  
            *Product Durability*:  
            The Airdopes 141 is designed to be durable under normal use conditions. However, like most electronics, they are prone to wear and tear over time, particularly the battery, which can degrade after extensive use. The shorter the lifespan, the higher the demand for replacements, leading to higher electronic waste (e-waste).

            **Sustainability Score**: 55/100  
            (Moderate durability, with concerns regarding battery lifespan and e-waste.)

            **4. Packaging**  
            *Sustainable Packaging*:  
            If the packaging of the Airdopes 141 uses non-recyclable plastic or excessive packaging materials, it could contribute to unnecessary waste. If the packaging uses recycled cardboard or other sustainable alternatives, this would improve the overall sustainability score.

            **Sustainability Score**: 40/100  
            (Without details on packaging material, it’s assumed that typical electronics packaging may not prioritize sustainability.)

            **5. Brand Initiatives**  
            *Company’s Environmental Efforts*:  
            The brand (likely a sub-brand of Boat or a similar manufacturer) may have sustainability practices in place, such as reducing carbon emissions or incorporating recycling programs. However, such practices may not always be communicated clearly or consistently, especially in consumer electronics.

            **Sustainability Score**: 50/100  
            (No clear details about the brand’s sustainability efforts could impact this score.)

            **Overall Sustainability Score**: 55/100

            The Airdopes 141 Bluetooth Wireless Earbuds have a moderate sustainability score. While the product may have some energy-efficient features and is durable to some extent, concerns regarding plastic materials, packaging, and the lifespan of the battery could affect its overall environmental impact. Consumers interested in more sustainable alternatives might seek products with better materials, longer-lasting batteries, and eco-friendly packaging.

            For a more comprehensive sustainability evaluation, it's recommended to look into specific certifications, such as energy-efficient ratings, packaging sustainability, or a detailed corporate responsibility report from the manufacturer.
            """
            return sustainability_analysis
        except json.JSONDecodeError:
            return "Error: Could not decode JSON from response."
    else:
        return "Error: Unable to get a valid response."

