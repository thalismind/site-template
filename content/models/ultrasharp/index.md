+++
date = '2025-01-06T03:02:29-06:00'
draft = false
title = 'Ultrasharp Experiment [Flux]'
summary = 'This is a detail enhancer for more photorealistic Flux images. These models are a series of experiments that I have done using different settings and optimizers to add more photographic detail to Flux.'
+++

{{< toc >}}

## Description

This is a detail enhancer for more photorealistic Flux images. These models are a series of experiments that I have done using different settings and optimizers to add more photographic detail to Flux.

The format for prompts is `ultrasharp photograph, [colors], [focus]`. You can specify one or two colors, like red or blue and red. The focus can be central focus or spread focus. Prompts should be relatively long and detailed, using the Llama/Joy style for descriptions.

### Features

- more individual leaves
- glowing sunlight
- finer wood grain
- better bokeh definition
- more even repeating patterns
- more detailed composition

## Gallery

{{< gallery >}}

## Download

### Ultrasharp v3 Flux

{{< tensor "ultrasharp-v03-flux" >}}

### Ultrasharp v2 Flux

{{< tensor "ultrasharp-v02-flux" >}}

## Recommended Parameters

- Model and CLIP strength from 0.25 - 1.1, depending on how much of an effect you want
- Flux guidance from 3.5 - 7.5

## Example Prompts

- {{< copy >}}ultrasharp photograph, brown and green, central focus. this is a highly detailed, macro photograph of a beetle, specifically a species of the family staphylinidae, resting on a green leaf. the beetle's body is a rich, burnished orange-brown color, with a glossy, almost metallic sheen that catches the light, creating subtle highlights and shadows. its exoskeleton is smooth and slightly textured, with visible segments and a defined, rounded shape. the beetle's head is prominent, featuring large, round, black eyes that are slightly reflective, giving it a somewhat alert expression. the antennae are long, slender, and segmented, extending outward from the head. the leaf it is resting on is a vibrant, fresh green with a fine, fuzzy texture, visible under magnification. the background is a soft, out of focus green, which helps to isolate the beetle and leaf, drawing attention to their intricate details. the photograph's sharp focus on the beetle and leaf contrasts with the out of focus background, enhancing the macro detail. the overall composition and lighting emphasize the beetle's striking appearance and the delicate textures of the leaf. the photograph captures a moment of stillness in nature, highlighting the intricate details of the beetle and the leaf it rests on.{{</ copy >}}
- {{< copy >}}ultrasharp photograph, gray, spread focus. this is a high-resolution photograph capturing the grand, gothic revival-style corridor of a historic building, likely a university or government building. the corridor features an impressive series of pointed arches, supported by robust, intricately carved stone columns, each adorned with classical motifs. the arches are constructed from polished, light gray stone with subtle variations in texture, suggesting a blend of marble and granite. the ceiling is vaulted, with a series of ribbed, semi-circular arches that converge at the apex, creating a sense of depth and perspective. the floor is made of large, polished stone tiles that run parallel to the corridor, contributing to the sense of grandeur and timelessness. on the right side of the image, there is a large, ornate wooden door with intricate carvings and a metal handle, suggesting it might be an entrance to a chamber or office. the door has a rich, dark brown color with a slightly glossy finish, contrasting beautifully with the stone architecture. on the left side, the corridor widens, revealing a series of tall, narrow windows with stone frames, allowing natural light to filter in, casting soft shadows and enhancing the architectural details. the overall atmosphere is one of historical significance, academic prestige, and timeless elegance.{{</ copy >}}
- {{< copy >}}ultrasharp photograph, red, central focus. this photograph captures a mesmerizing, high-resolution image of a single water droplet suspended in mid-air above a circular pool of water, creating a perfect, smooth, concentric ripple effect. the droplet is a perfect sphere, reflecting light and showing a slight curvature, with a glossy, almost metallic texture, indicating the water's surface tension. the pool of water beneath it is a deep, rich red, with subtle variations in hue and saturation, giving it a velvety, almost liquid texture. the background is a gradient of deep reds, transitioning from a darker, almost black shade at the top to a lighter, more vibrant red at the bottom, creating a sense of depth and dimension. the overall composition is simple yet striking, with the droplet being the focal point and the red hues providing a cohesive, dramatic color scheme. the lighting is soft yet directional, casting subtle shadows and highlights that enhance the droplet's three-dimensional appearance. the photograph exudes a sense of fluidity and elegance, with a strong emphasis on the droplet's delicate, suspended form.{{</ copy >}}
- {{< copy >}}ultrasharp photograph, white and green, central focus. this photograph captures a serene, rural landscape dominated by a quaint, white, single-story cottage nestled in a vast, open field. the cottage, centrally positioned, features a steep, dark grey slate roof with several small, square windows and a black door. the structure appears rustic and charming, with a chimney extending from the roof's right side. the field surrounding the cottage is a lush, golden-brown grassland, slightly overgrown and wild, with tall, swaying grasses that seem to gently sway, hinting at a light breeze. the background is dominated by a majestic, rugged mountain range with steep, rocky slopes that transition into a verdant, green plateau at the top. the mountain's texture is rough, with exposed rock and patches of green vegetation, indicating a high altitude and possibly a remote, isolated location. the sky above is a dramatic, moody backdrop, filled with a mix of dark, stormy clouds and lighter, wispy cirrus clouds, suggesting an impending change in weather. the trees, sparse but dense, are a dark, rich green, adding depth to the scene and framing the cottage. the overall mood is tranquil yet slightly foreboding, evoking a sense of isolation and natural beauty. the photograph captures the essence of rural, highland scenery in a raw, untouched state.{{</ copy >}}

## Changelog

### v3

The Ultrasharp Flux experiment continues with a new version, this time using the Ranger21 optimizer to transfer a sharp, realistic style without changing your images too much.

https://github.com/lessw2020/Ranger21

Note: some color banding in very dark areas and areas of even color, almost like compression artifacts. This occurs more during hires. You can reduce the effect of these bugs by disabling the lora during the hires pass.

These artifacts were not present in the training data, so I am not sure where they came from, but it seems like they might be related to the bokeh and background focus effects.

### v2

This is an experimental LoRA that I trained on a series of high resolution photographs with a focus on extremely sharp details and muted colors. I am not completely happy with the results, but they are interesting enough to share, I think.
