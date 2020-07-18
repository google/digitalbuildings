package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IChilled;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IChilled_supply_water_temperature_sensor extends IField{

	public IRI iri();

    public void addComposedOfChilled (IChilled parameter);

	public Set<IChilled> getComposedOfChilled();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

    public void addComposedOfTemperature (ITemperature parameter);

	public Set<ITemperature> getComposedOfTemperature();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}