package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.ICapacity;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;
import www.google.com.digitalbuildings._0_0_1.subfields.IThermal;

public interface ICooling_thermal_power_capacity extends IField{

	public IRI iri();

    public void addComposedOfCapacity (ICapacity parameter);

	public Set<ICapacity> getComposedOfCapacity();

    public void addComposedOfCooling (ICooling parameter);

	public Set<ICooling> getComposedOfCooling();

    public void addComposedOfPower (IPower parameter);

	public Set<IPower> getComposedOfPower();

    public void addComposedOfThermal (IThermal parameter);

	public Set<IThermal> getComposedOfThermal();

}