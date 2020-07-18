package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWind;
import www.google.com.digitalbuildings._0_0_1.subfields.ILinearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.IEast;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IEast_wind_linearvelocity_sensor extends IField{

	public IRI iri();

    public void addComposedOfEast (IEast parameter);

	public Set<IEast> getComposedOfEast();

    public void addComposedOfLinearvelocity (ILinearvelocity parameter);

	public Set<ILinearvelocity> getComposedOfLinearvelocity();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWind (IWind parameter);

	public Set<IWind> getComposedOfWind();

}