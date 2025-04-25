#!/usr/bin/env python3
"""
Generate and display the circuit schematic diagram using Plotly.
"""
import plotly.graph_objects as go

def main():
    fig = go.Figure()

    # Draw power and ground rails
    fig.add_shape(type="line", x0=0, y0=5, x1=10, y1=5,
                  line=dict(color="red", width=4))
    fig.add_annotation(x=0, y=5.2, text="+5V", showarrow=False, font=dict(color="red"))

    fig.add_shape(type="line", x0=0, y0=0, x1=10, y1=0,
                  line=dict(color="black", width=4))
    fig.add_annotation(x=0, y=-0.2, text="GND", showarrow=False)

    # LDR branch (voltage divider)
    fig.add_shape(type="line", x0=2, y0=5, x1=2, y1=3,
                  line=dict(color="black", width=2))
    fig.add_annotation(x=2.3, y=4, text="LDR", showarrow=False)
    fig.add_shape(type="line", x0=2, y0=3, x1=2, y1=1,
                  line=dict(color="black", width=2))
    fig.add_annotation(x=2.3, y=2, text="10kΩ", showarrow=False)
    # Connection to Arduino A5
    fig.add_shape(type="line", x0=2, y0=3, x1=6, y1=3,
                  line=dict(color="blue", width=2))
    fig.add_annotation(x=6.2, y=3, text="A5", showarrow=False)

    # LED branch
    fig.add_shape(type="line", x0=8, y0=5, x1=8, y1=3,
                  line=dict(color="black", width=2))
    fig.add_annotation(x=8.3, y=4, text="220Ω", showarrow=False)
    fig.add_shape(type="line", x0=8, y0=3, x1=8, y1=1,
                  line=dict(color="black", width=2))
    fig.add_annotation(x=8.3, y=2, text="LED", showarrow=False)
    # Connection to Arduino D2
    fig.add_shape(type="line", x0=8, y0=1, x1=6, y1=1,
                  line=dict(color="blue", width=2))
    fig.add_annotation(x=6.2, y=1, text="D2", showarrow=False)

    # Layout adjustments
    fig.update_xaxes(visible=False, range=[-1, 11])
    fig.update_yaxes(visible=False, range=[-1, 6])
    fig.update_layout(showlegend=False, title="Circuit Schematic: LED ↔ LDR Data Link")
    fig.show()

if __name__ == "__main__":
    main()