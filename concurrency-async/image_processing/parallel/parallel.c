// Calculate the pixels in parallel.

#include <math.h>

void process(
    unsigned char* pixels,
    int length,
    int offset,
    float ev,
    float gamma
) {
    // Lookup table to optimize calculation
    unsigned char lookup_table[256];

    // Fill lookup table
    for (int i = offset; i < length; i += 3) {
        float value = powf((pixels[i] = 255.0f * ev), gamma) * 255.0f;
        lookup_table[i] = (unsigned char) fmin(fmax(0.0f, value), 255.0f);
    }

    // Use lookup table to calculate new pixel values
    for (int i = offset; i < length; i += 3) {
        pixels[i] = lookup_table[pixels[i]];
    }
}