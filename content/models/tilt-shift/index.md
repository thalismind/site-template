+++
date = '2025-04-03T06:00:00-06:00'
draft = false
title = 'Tilt Shift / Miniature Diorama [Flux]'
summary = 'A photo effect using the Ranger21 optimizer to apply a strong style transfer with good prompt adherence. This keeps a narrow part of the image in focus, while blurring the rest.'
+++

{{< toc >}}

## Description

Another photo effect using the Ranger21 optimizer to apply a strong style transfer with good prompt adherence. This keeps a narrow part of the image in focus, while blurring the rest. Occasionally it will get confused and blur the entire image.

https://github.com/lessw2020/Ranger21

> {{< colorful color="green" >}}
When remixing Flux images, make sure to use a reasonable CFG value. It will often default to 1.0, which does not look good. Using 3.5 or 4.0 will look better.
{{< /colorful >}}

## Gallery

{{< gallery >}}

## Download

### Tilt Shift v1 Flux

{{< tensor "tilt-shift-v01-flux" >}}

## Recommended Parameters

- Model and CLIP strength from 0.25 - 1.1, depending on how much of an effect you want
- Flux guidance from 3.5 - 7.5

## Example Prompts

- {{< copy >}}A photo-realistic depiction of a figurine scene featuring a lone figure of a man with a beard and a long beard, wearing a brown robe, standing in the middle of a grassy field with a blurred background of mountains and greenery. the figure appears to be a man, with a serious expression, and is positioned in the center of the image. he is wearing a long robe and a hood, and his hands are clasped together in front of him. surrounding him are several small, detailed figurines of dogs, all of which appear to be grey in color and have a realistic appearance. the figures are arranged in a line, with the man standing out from the rest, and they are all facing the same direction. the scene is set in a mountainous landscape, with trees and rocks scattered throughout, and the overall atmosphere is peaceful and serene.{{< /copy >}}
- {{< copy >}}A photo-realistic shoot from a bird's eye view about a small red toy car, driving on a city street. the car is positioned at the center of the image, positioned in the middle of the frame, with a blurred cityscape in the background. it appears to be a small, red and white toy vehicle with a blue and white stripe running along its side, and it is positioned on the right side of the street. on the left side, there is a yellow traffic cone and a yellow and white striped barricade. the image is taken from a high angle, looking down on the car, giving a sense of depth and perspective. the background is slightly out of focus, but it seems to be an urban setting with blurred buildings and people in the distance.{{< /copy >}}
- {{< copy >}}A photo-realistic shoot from a bird's eye view of a city street at night, featuring a blurred cityscape with a large blue building in the background. the image is taken from a high angle, looking down on the cityscape, with a shallow depth of field that highlights the details of the buildings, vehicles, and trees. in the foreground, a small black car is driving on a zebra crossing, while a small white car is in the middle of the image. the car appears to be a minivan, and it is moving towards the right side of the frame. the scene is illuminated by the soft, blurry lights of the city, creating a sense of movement and energy. the background features a large crowd of cars parked in a parking lot, and a traffic light with a blue light, which is slightly out of focus, adding to the sense of depth and dimensionality. the overall effect is one of a bustling cityscape at night with a lot of lights and motion blur, giving the image a dreamy, ethereal quality.{{< /copy >}}
- {{< copy >}}A photo-realistic shoot from a bird's eye view about an urban landscape at night, featuring a cityscape with multiple buildings and lights. the image is taken from a low angle, focusing on the cityscape, with a focus on the buildings and the lights. in the center of the image, a large, modern building with a glass facade is visible, surrounded by smaller buildings with a red roof. the building on the left has a tall, rectangular shape, while the one on the right has a rectangular shape. the buildings are lit up with warm, orange and yellow lights, creating a bokeh effect around them. the background is blurred, with buildings and trees visible, giving the image a dreamy, ethereal quality.{{< /copy >}}
