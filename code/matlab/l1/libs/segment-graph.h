/*
Copyright (C) 2006 Pedro Felzenszwalb

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
*/

#ifndef SEGMENT_GRAPH
#define SEGMENT_GRAPH

#include <algorithm>
#include <cmath>
#include "disjoint-set.h"
// #include <opencv2/opencv.hpp>
// using namespace cv;
// threshold function
#define THRESHOLD(size, c) (c/size)
// a, b: the vertices connected by this edge
// w: the weight
typedef struct {
    float w;
    int a, b;
} edge;

bool operator<(const edge &a, const edge &b) {
    return a.w < b.w;
}

/*
* Check whether two clusters are allowed to merge: if the total number of
* of pixels exceed max_pixel_num, merge is not allowed.
*
* u: disjoint set
* a: label for first cluster
* b: label for second cluster
* max_pixel_num: maximum number of pixels in a cluster
*/
bool AllowMerge(const universe& u, int a, int b, int max_pixel_num, image<int>* region){
    int size_a = u.size(a);
    int size_b = u.size(b);
    int width = region->width();
    if (size_a + size_b > max_pixel_num) {
        return false;
    }

    int y_a = a / width;
    int x_a = a % width;
    int y_b = b / width;
    int x_b = b % width;
    if (region->access[y_a][x_a] != region->access[y_b][x_b]){
        return false;
    }
    
    return true;
}

/*
* Segment a graph
*
* Returns a disjoint-set forest representing the segmentation.
*
* num_vertices: number of vertices in graph.
* num_edges: number of edges in graph
* edges: array of edges.
* c: constant for treshold function.
* max_pixel_num: maximum number of pixels in a cluster
*/
universe *segment_graph(int num_vertices, int num_edges, edge *edges,
    float c, int max_pixel_num, image<int>* region) {
    // sort edges by weight
    std::sort(edges, edges + num_edges);

    // make a disjoint-set forest
    universe *u = new universe(num_vertices);

    // init thresholds
    float *threshold = new float[num_vertices];
    for (int i = 0; i < num_vertices; i++)
        threshold[i] = THRESHOLD(1, c);

    // for each edge, in non-decreasing weight order...
    for (int i = 0; i < num_edges; i++) {
        edge *pedge = &edges[i];

        // components conected by this edge
        int a = u->find(pedge->a);
        int b = u->find(pedge->b);
        if (a != b) {
            if ((pedge->w <= threshold[a]) &&
                (pedge->w <= threshold[b]) &&
                AllowMerge(*u, a, b, max_pixel_num, region) == true) {
                u->join(a, b);
                a = u->find(a);
                threshold[a] = pedge->w + THRESHOLD(u->size(a), c);
            }
        }
    }

    // free up
    delete threshold;
    return u;
}


#endif
