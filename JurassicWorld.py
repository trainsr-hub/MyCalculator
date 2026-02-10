def show_graph(C, x_point=None, y_point=None, Optimal_x=None):    
  
    if C <= 0:    
        st.warning("No positive solution region.")    
        return    
  
    x_max = max(C / 3.2, x_point + 25)    
    real_x = C / (1 + 3.2)  
    real_minx = C / (10 + 3.2)  
    y_max = max(C, y_point)  
    y_max_real = y_max - real_minx * 3.2  
  
    x = np.linspace(0, x_max, 400)    
    y = C - 3.2 * x    
  
    fig, ax = plt.subplots()    
  
    # =========================    
    # VÙNG NON-RED (≤ C)    
    # =========================    
  
    if Optimal_x is not None:    
  
        # Giới hạn các mốc trong [0, x_max]    
        x1 = max(0, min(x_max, Optimal_x / 2))    
        x2 = max(0, min(x_max, Optimal_x / 1.5))    
        x3 = max(0, min(x_max, Optimal_x / 1.13))    
        x4 = max(0, min(x_max, Optimal_x * 1.13))    
        x5 = max(0, min(x_max, Optimal_x * 1.5))    
        x6 = max(0, min(x_max, Optimal_x * 2))    
  
        # Mask từng đoạn    
        mask1 = (x > 0) & (x <= x1)    
        mask2 = (x > x1) & (x <= x2)    
        mask3 = (x > x2) & (x <= x3)    
        mask4 = (x > x3) & (x <= x4)    
        mask5 = (x > x4) & (x <= x5)    
        mask6 = (x > x5) & (x <= x6)    
        mask7 = (x > x6) & (x <= x_max)    
  
        ax.fill_between(    
            x[mask1],    
            0,    
            y[mask1],    
            color="#00ffff",    
            alpha=1  
        )    
  
  
        ax.fill_between(    
            x[mask2],    
            0,    
            y[mask2],    
            color="purple",    
            alpha=0.7  
        )    
  
        ax.fill_between(    
            x[mask3],    
            0,    
            y[mask3],    
            color="blue",    
            alpha=1    
        )    
  
        ax.fill_between(    
            x[mask4],    
            0,    
            y[mask4],    
            color="lime",  
            alpha=1    
        )    
  
        ax.fill_between(    
            x[mask5],    
            0,    
            y[mask5],    
            color="yellow",    
            alpha=1  
        )    
        ax.fill_between(    
            x[mask6],    
            0,    
            y[mask6],    
            color="red",    
            alpha=1    
        )    
        ax.fill_between(    
            x[mask7],    
            0,    
            y[mask7],    
            color="gray",    
            alpha=0.6  
        )    
    else:    
        ax.fill_between(x, 0, y, alpha=0.3)    
  
    # =========================    
    # VÙNG RED (> C)    
    # =========================    
    ax.fill_between(x, y, y_max, color="red", alpha=0.4)    
  
    ax.plot(x, y)    
  
    # =========================    
    # PHẦN ĐIỂM & GIAO    
    # =========================    
  
    if x_point is not None and y_point is not None:    
  
        ax.scatter(x_point, y_point, s=100, zorder=5)    
  
        ax.annotate(    
            f"({x_point}, {y_point})",    
            (x_point, y_point),    
            xytext=(5, 5),    
            textcoords="offset points"    
        )    
  
        ax.axvline(x=x_point, linestyle="--")    
        ax.axhline(y=y_point, linestyle="--")    
  
        y_intersect = int(C - 3.2 * x_point)    
        ax.scatter(x_point, y_intersect, zorder=6)    
  
        ax.annotate(    
            f"Máu trâu\n({x_point}, {y_intersect})",    
            (x_point, y_intersect),    
            xytext=(5, -25),    
            textcoords="offset points"    
        )    
  
        x_intersect = int((C - y_point) / 3.2)    
        ax.scatter(x_intersect, y_point, zorder=6)    
  
        ax.annotate(    
            f"Damage to\n({x_intersect}, {y_point})",    
            (x_intersect, y_point),    
            xytext=(5, 10),    
            textcoords="offset points"    
        )    
  
    ax.set_xlim(min(y_max, real_minx), real_x)    
    ax.set_ylim(min(y_max, real_minx), y_max_real)   
  
    ax.set_title(f"3.2x + y = {int(C)}")    
    ax.set_xlabel("ATK")    
    ax.grid(False)    
  
    st.pyplot(fig)    
    show_legend()