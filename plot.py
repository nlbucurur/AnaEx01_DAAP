import ROOT

# Open the .root file
file = ROOT.TFile("build/AnaEx01.root")

# Retrieve the histograms
h1 = file.Get("histo/EAbs")
h2 = file.Get("histo/EAbsSec")

# Check if histograms exist
if not h1 or not h2:
    print("Error: Histograms not found in the file")
    exit()

# Create a canvas
c1 = ROOT.TCanvas("c1", "Histograms Overlay", 800, 600)

# Set axis labels for the first histogram (it sets for both since they share the same canvas)
h1.GetXaxis().SetTitle("Energy deposited (%)")
h1.GetYaxis().SetTitle("Frequency")

# Enable statistics boxes
ROOT.gStyle.SetOptStat(1111)

# Draw the first histogram with lines between points
h1.SetLineColor(ROOT.kRed) # Set the line color for the first histogram
h1.Draw("HIST")

# Draw the second histogram with lines between points on the same canvas
h2.SetLineColor(ROOT.kBlue) # Set the line color for the second histogram
h2.Draw("SAME HIST")

# Update the canvas to reflect the changes
c1.Update()

# Move the statistics box of the first histogram
st1 = h1.GetListOfFunctions().FindObject("stats")
if st1:
    st1.SetX1NDC(0.72)  # Set X1 position
    st1.SetY1NDC(0.8)   # Set Y1 position
    st1.SetX2NDC(0.92)  # Set X2 position
    st1.SetY2NDC(0.9)   # Set Y2 position

# Move the statistics box of the second histogram
st2 = h2.GetListOfFunctions().FindObject("stats")
if st2:
    st2.SetX1NDC(0.72)  # Set X1 position
    st2.SetY1NDC(0.6)   # Set Y1 position
    st2.SetX2NDC(0.92)  # Set X2 position
    st2.SetY2NDC(0.7)   # Set Y2 position

# Update the canvas to reflect the changes
c1.Modified()
c1.Update()

# Save the canvas as an image
# c1.SaveAs("overlayed_histograms.png")

# Keep the canvas open
c1.Draw()
input("Press Enter to exit...")