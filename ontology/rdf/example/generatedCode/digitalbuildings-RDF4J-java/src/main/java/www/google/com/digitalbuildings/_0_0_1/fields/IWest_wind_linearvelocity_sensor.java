package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWind;
import www.google.com.digitalbuildings._0_0_1.subfields.IWest;
import www.google.com.digitalbuildings._0_0_1.subfields.ILinearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IWest_wind_linearvelocity_sensor extends IField{

	public IRI iri();

    public void addComposedOfLinearvelocity (ILinearvelocity parameter);

	public Set<ILinearvelocity> getComposedOfLinearvelocity();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWest (IWest parameter);

	public Set<IWest> getComposedOfWest();

    public void addComposedOfWind (IWind parameter);

	public Set<IWind> getComposedOfWind();

}