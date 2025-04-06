// Calculate the pixels in parallel.

#include <math.h>

void process(
    unsigned char* pixels,
    int length,
    float ev,
    float gamma
) {
    // Starting of `offset` and the step size of 3 allows each worker
    // thread to work independently of the other (two) threads.
    for (int i = offset; i < length; i += 3) {
        float value = powf((pixels[i] = 255.0f * ev), gamma) * 255.0f;
        pixels[i] = (unsigned char) fmin(fmax(0.0f, value), 255.0f);
    }
}