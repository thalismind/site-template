# Image/Tensor Gallery Site Template

This is a basic template for a https://gohugo.io/ site with image galleries, download cards, and
an optional download limit worker.

The image galleries include image metadata such as the prompt and generation parameters for
AI-generated images. The download cards include training metadata such as the learning rate
and dataset size for models in the `.safetensors` format. The optional download worker uses
a per-user token system to limit the number of downloads for each person and users can be
allowed to download pre-release models or prevented from doing so.

Following the standard Hugo folder structure, the template includes a `content` folder with
some example posts for image galleries and tensor models. Shortcodes are included for the
image galleries, download cards, and to show or hide adult content.

## Documentation

- [setup guide](./docs/setup.md)

## License

This template is licensed under the AGPL license. In short, this means that the template is open
source, but any changes that you make have to be contributed back to this repository or published
in a fork with the same license. You cannot modify and use this template to create a commercial
site without making your changes available under the same open source license.
