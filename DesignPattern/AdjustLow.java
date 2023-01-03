public class AdjustLow implements AdjustColorIntensity {
    protected String tonerSavingLevel;
    protected String colorIntensity;
    @Override
    public void adjustColorIntensity() {
         if(tonerSavingLevel=="low"){
            colorIntensity="slightly reduced";
        }
    }
}
